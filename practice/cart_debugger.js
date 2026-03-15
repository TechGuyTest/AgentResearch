#!/usr/bin/env node
/**
 * Debug Practice Exercise: Shopping Cart Calculator
 * Contains several intentional bugs for debugging practice.
 * Try to find and fix all issues!
 * 
 * Problems to look for:
 * 1. Logic error in discount calculation
 * 2. Floating-point precision issue
 * 3. Missing edge case handling (empty cart, negative quantities)
 * 4. Inefficient pattern (nested loops)
 * 5. Type coercion bug
 * 6. Missing input validation
 */

/**
 * Calculate subtotal for items in cart
 * @param {Array} items - Array of item objects with price and quantity
 * @returns {number} Subtotal amount
 */
function calculateSubtotal(items) {
    let subtotal = 0;
    
    // Problem 1: No validation for empty array or invalid items
    for (let i = 0; i <= items.length; i++) {  // BUG: <= should be <
        subtotal += items[i].price * items[i].quantity;
    }
    
    return subtotal;
}

/**
 * Apply discount based on total amount
 * @param {number} total - Total amount before discount
 * @param {string} discountCode - Discount code
 * @returns {number} Discounted amount
 */
function applyDiscount(total, discountCode) {
    let discount = 0;
    
    // Problem 2: Missing validation for discountCode type
    if (discountCode === 'SAVE10') {
        discount = total * 0.1;
    } else if (discountCode === 'SAVE20') {
        discount = total * 0.2;
    } else if (discountCode === 'SAVE50') {
        // Problem 3: Logic error - should be 0.5, not 0.05
        discount = total * 0.05;  // BUG: 5% instead of 50%
    }
    
    // Problem 4: Floating-point precision issue
    return total - discount;
}

/**
 * Calculate shipping cost based on cart weight
 * @param {Array} items - Array of item objects with weight and quantity
 * @returns {number} Shipping cost
 */
function calculateShipping(items) {
    let totalWeight = 0;
    
    // Problem 5: Inefficient - recalculating length on each iteration
    for (let i = 0; i < items.length; i++) {
        // Problem 6: No check for undefined weight
        totalWeight += items[i].weight * items[i].quantity;
    }
    
    // Problem 7: No validation for negative weight
    if (totalWeight < 2) {
        return 5.00;
    } else if (totalWeight < 5) {
        return 10.00;
    } else {
        return 15.00;
    }
}

/**
 * Check if cart contains out-of-stock items
 * @param {Array} items - Array of item objects
 * @param {Array} inventory - Array of available items with stock
 * @returns {Array} Array of out-of-stock item names
 */
function checkStock(items, inventory) {
    const outOfStock = [];
    
    // Problem 8: Inefficient nested loop - O(n*m) complexity
    for (let i = 0; i < items.length; i++) {
        let found = false;
        
        for (let j = 0; j < inventory.length; j++) {
            // Problem 9: Type coercion bug - using == instead of ===
            if (inventory[j].id == items[i].id) {  // BUG: == can cause unexpected matches
                if (inventory[j].stock < items[i].quantity) {
                    outOfStock.push(items[i].name);
                }
                found = true;
                break;
            }
        }
        
        // Problem 10: Missing case when item not found in inventory
        if (!found) {
            // Should also add to outOfStock, but doesn't
        }
    }
    
    return outOfStock;
}

/**
 * Format currency amount
 * @param {number} amount - Amount to format
 * @returns {string} Formatted currency string
 */
function formatCurrency(amount) {
    // Problem 11: No validation for amount type
    // Problem 12: Floating-point display issue
    return '$' + amount.toFixed(2);
}

/**
 * Main cart calculator
 * @param {Object} cart - Cart object with items and discount code
 * @param {Array} inventory - Inventory data
 * @returns {Object} Cart summary with totals
 */
function calculateCartTotal(cart, inventory) {
    // Problem 13: No validation for cart structure
    const subtotal = calculateSubtotal(cart.items);
    const discounted = applyDiscount(subtotal, cart.discountCode);
    const shipping = calculateShipping(cart.items);
    const outOfStockItems = checkStock(cart.items, inventory);
    
    // Problem 14: Floating-point addition precision
    const total = discounted + shipping;
    
    return {
        subtotal: formatCurrency(subtotal),
        discount: formatCurrency(subtotal - discounted),
        shipping: formatCurrency(shipping),
        total: formatCurrency(total),
        outOfStockItems: outOfStockItems
    };
}

// Test data with edge cases
const testInventory = [
    { id: 1, name: 'Laptop', stock: 10 },
    { id: 2, name: 'Mouse', stock: 50 },
    { id: 3, name: 'Keyboard', stock: 20 },
    { id: 4, name: 'Monitor', stock: 0 },  // Out of stock
    { id: 5, name: 'Headphones', stock: 3 }
];

const testCart = {
    items: [
        { id: 1, name: 'Laptop', price: 999.99, weight: 2.5, quantity: 1 },
        { id: 2, name: 'Mouse', price: 25.50, weight: 0.2, quantity: 2 },
        { id: 4, name: 'Monitor', price: 299.99, weight: 5.0, quantity: 1 },  // Out of stock
        { id: 5, name: 'Headphones', price: 79.99, weight: 0.5, quantity: 5 }  // More than stock
    ],
    discountCode: 'SAVE50'  // Should give 50% off
};

// Edge case: empty cart
const emptyCart = {
    items: [],
    discountCode: ''
};

// Edge case: negative quantity
const invalidCart = {
    items: [
        { id: 1, name: 'Laptop', price: 999.99, weight: 2.5, quantity: -1 }  // Invalid!
    ],
    discountCode: 'SAVE10'
};

// Run tests
console.log('=== Shopping Cart Calculator Debug Exercise ===\n');

console.log('1. Normal cart calculation:');
try {
    const result = calculateCartTotal(testCart, testInventory);
    console.log('   Subtotal:', result.subtotal);
    console.log('   Discount:', result.discount);
    console.log('   Shipping:', result.shipping);
    console.log('   Total:', result.total);
    console.log('   Out of stock:', result.outOfStockItems.join(', ') || 'None');
} catch (error) {
    console.log('   ❌ Error:', error.message);
}

console.log('\n2. Empty cart:');
try {
    const result = calculateCartTotal(emptyCart, testInventory);
    console.log('   Subtotal:', result.subtotal);
    console.log('   Total:', result.total);
} catch (error) {
    console.log('   ❌ Error:', error.message);
}

console.log('\n3. Invalid cart (negative quantity):');
try {
    const result = calculateCartTotal(invalidCart, testInventory);
    console.log('   Subtotal:', result.subtotal);
    console.log('   Total:', result.total);
} catch (error) {
    console.log('   ❌ Error:', error.message);
}

console.log('\n4. Floating-point precision test:');
const price1 = 0.1;
const price2 = 0.2;
console.log('   0.1 + 0.2 =', price1 + price2);  // Should be 0.3, but isn't!
console.log('   Expected: 0.3');

console.log('\n💡 Hints for debugging:');
console.log('   - Check loop boundaries carefully');
console.log('   - Look for type coercion issues (== vs ===)');
console.log('   - Test with edge cases (empty, negative, zero)');
console.log('   - Watch out for floating-point arithmetic');
console.log('   - Validate all inputs before processing');
