/**
 * Unit Tests for Shopping Cart Calculator
 * These tests verify the bug fixes in cart_debugger.js
 */

const {
    calculateSubtotal,
    applyDiscount,
    calculateShipping,
    checkStock,
    formatCurrency,
    calculateCartTotal
} = require('./cart_debugger.js');

// Simple test framework
let passed = 0;
let failed = 0;

function test(name, fn) {
    try {
        fn();
        console.log(`✓ ${name}`);
        passed++;
    } catch (error) {
        console.log(`✗ ${name}`);
        console.log(`  Error: ${error.message}`);
        failed++;
    }
}

function assertEqual(actual, expected, message) {
    if (actual !== expected) {
        throw new Error(`${message || 'Assertion failed'}: expected ${expected}, got ${actual}`);
    }
}

function assertThrows(fn, message) {
    try {
        fn();
        throw new Error(message || 'Expected function to throw');
    } catch (error) {
        // Expected
    }
}

console.log('=== Cart Debugger Tests ===\n');

// Tests for calculateSubtotal
console.log('--- calculateSubtotal ---');

test('calculateSubtotal: normal items', () => {
    const items = [
        { price: 10, quantity: 2 },
        { price: 20, quantity: 1 }
    ];
    assertEqual(calculateSubtotal(items), 40, 'Should calculate correct subtotal');
});

test('calculateSubtotal: empty array', () => {
    assertEqual(calculateSubtotal([]), 0, 'Should return 0 for empty array');
});

test('calculateSubtotal: null items', () => {
    assertEqual(calculateSubtotal(null), 0, 'Should return 0 for null');
});

test('calculateSubtotal: negative quantity throws error', () => {
    const items = [{ price: 10, quantity: -1 }];
    assertThrows(() => calculateSubtotal(items), 'Should throw for negative quantity');
});

test('calculateSubtotal: invalid item structure throws error', () => {
    const items = [{ price: 'invalid', quantity: 1 }];
    assertThrows(() => calculateSubtotal(items), 'Should throw for invalid price type');
});

// Tests for applyDiscount
console.log('\n--- applyDiscount ---');

test('applyDiscount: SAVE10 code', () => {
    assertEqual(applyDiscount(100, 'SAVE10'), 90, 'Should apply 10% discount');
});

test('applyDiscount: SAVE20 code', () => {
    assertEqual(applyDiscount(100, 'SAVE20'), 80, 'Should apply 20% discount');
});

test('applyDiscount: SAVE50 code (BUG FIX)', () => {
    assertEqual(applyDiscount(100, 'SAVE50'), 50, 'Should apply 50% discount (was 5% before fix)');
});

test('applyDiscount: invalid code returns original', () => {
    assertEqual(applyDiscount(100, 'INVALID'), 100, 'Should return original for invalid code');
});

test('applyDiscount: empty code returns original', () => {
    assertEqual(applyDiscount(100, ''), 100, 'Should return original for empty code');
});

test('applyDiscount: negative total throws error', () => {
    assertThrows(() => applyDiscount(-100, 'SAVE10'), 'Should throw for negative total');
});

test('applyDiscount: floating-point precision (BUG FIX)', () => {
    const result = applyDiscount(100.10, 'SAVE10');
    assertEqual(result, 90.09, 'Should handle floating-point correctly');
});

// Tests for calculateShipping
console.log('\n--- calculateShipping ---');

test('calculateShipping: empty array', () => {
    assertEqual(calculateShipping([]), 0, 'Should return 0 for empty cart');
});

test('calculateShipping: light weight (< 2)', () => {
    const items = [{ weight: 0.5, quantity: 1 }];
    assertEqual(calculateShipping(items), 5.00, 'Should charge $5 for weight < 2');
});

test('calculateShipping: medium weight (2-5)', () => {
    const items = [{ weight: 3, quantity: 1 }];
    assertEqual(calculateShipping(items), 10.00, 'Should charge $10 for weight 2-5');
});

test('calculateShipping: heavy weight (> 5)', () => {
    const items = [{ weight: 6, quantity: 1 }];
    assertEqual(calculateShipping(items), 15.00, 'Should charge $15 for weight > 5');
});

test('calculateShipping: negative weight throws error', () => {
    const items = [{ weight: -1, quantity: 1 }];
    assertThrows(() => calculateShipping(items), 'Should throw for negative weight');
});

// Tests for checkStock
console.log('\n--- checkStock ---');

test('checkStock: items in stock', () => {
    const items = [{ id: 1, name: 'Laptop', quantity: 1 }];
    const inventory = [{ id: 1, name: 'Laptop', stock: 10 }];
    const result = checkStock(items, inventory);
    assertEqual(result.length, 0, 'Should have no out of stock items');
});

test('checkStock: items out of stock', () => {
    const items = [{ id: 1, name: 'Laptop', quantity: 5 }];
    const inventory = [{ id: 1, name: 'Laptop', stock: 2 }];
    const result = checkStock(items, inventory);
    assertEqual(result.length, 1, 'Should detect out of stock item');
    assertEqual(result[0], 'Laptop', 'Should return correct item name');
});

test('checkStock: item not in inventory (BUG FIX)', () => {
    const items = [{ id: 999, name: 'Unknown', quantity: 1 }];
    const inventory = [{ id: 1, name: 'Laptop', stock: 10 }];
    const result = checkStock(items, inventory);
    assertEqual(result.length, 1, 'Should mark unknown items as out of stock');
});

test('checkStock: strict equality (BUG FIX)', () => {
    // Test that == vs === matters - using string vs number id
    const items = [{ id: '1', name: 'Laptop', quantity: 1 }];
    const inventory = [{ id: 1, name: 'Laptop', stock: 10 }];
    const result = checkStock(items, inventory);
    // With ===, these won't match, so item should be out of stock
    assertEqual(result.length, 1, 'Should use strict equality');
});

test('checkStock: empty items array', () => {
    const result = checkStock([], [{ id: 1, stock: 10 }]);
    assertEqual(result.length, 0, 'Should return empty for empty items');
});

// Tests for formatCurrency
console.log('\n--- formatCurrency ---');

test('formatCurrency: normal amount', () => {
    assertEqual(formatCurrency(10.5), '$10.50', 'Should format correctly');
});

test('formatCurrency: integer amount', () => {
    assertEqual(formatCurrency(10), '$10.00', 'Should add decimal places');
});

test('formatCurrency: floating-point precision (BUG FIX)', () => {
    const result = formatCurrency(0.1 + 0.2);
    assertEqual(result, '$0.30', 'Should handle 0.1 + 0.2 correctly');
});

test('formatCurrency: invalid type throws error', () => {
    assertThrows(() => formatCurrency('invalid'), 'Should throw for non-number');
});

// Tests for calculateCartTotal
console.log('\n--- calculateCartTotal ---');

test('calculateCartTotal: normal cart', () => {
    const cart = {
        items: [{ id: 1, name: 'Item', price: 100, weight: 1, quantity: 1 }],
        discountCode: 'SAVE10'
    };
    const inventory = [{ id: 1, stock: 10 }];
    const result = calculateCartTotal(cart, inventory);
    assertEqual(result.subtotal, '$100.00', 'Should calculate subtotal');
    assertEqual(result.discount, '$10.00', 'Should calculate discount');
    assertEqual(result.shipping, '$5.00', 'Should calculate shipping');
});

test('calculateCartTotal: invalid cart throws error', () => {
    assertThrows(() => calculateCartTotal(null, []), 'Should throw for null cart');
    assertThrows(() => calculateCartTotal({}, []), 'Should throw for cart without items');
});

test('calculateCartTotal: empty cart', () => {
    const cart = { items: [], discountCode: '' };
    const result = calculateCartTotal(cart, []);
    assertEqual(result.subtotal, '$0.00', 'Should handle empty cart');
    assertEqual(result.total, '$0.00', 'Total should be 0');
});

// Summary
console.log('\n=== Test Summary ===');
console.log(`Passed: ${passed}`);
console.log(`Failed: ${failed}`);
console.log(`Total: ${passed + failed}`);

if (failed > 0) {
    process.exit(1);
}
