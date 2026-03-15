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
    // Validate input - handle empty array
    if (!items || items.length === 0) {
        return 0;
    }
    
    let subtotal = 0;
    
    // Fixed: Changed <= to < to avoid accessing undefined
    for (let i = 0; i < items.length; i++) {
        // Validate item structure and quantity
        if (!items[i] || typeof items[i].price !== 'number' || typeof items[i].quantity !== 'number') {
            throw new Error(`Invalid item at index ${i}: must have numeric price and quantity`);
        }
        // Reject negative quantities
        if (items[i].quantity < 0) {
            throw new Error(`Invalid quantity at index ${i}: quantity cannot be negative`);
        }
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
    // Validate input types
    if (typeof total !== 'number' || isNaN(total)) {
        throw new Error('Invalid total: must be a number');
    }
    if (total < 0) {
        throw new Error('Invalid total: cannot be negative');
    }
    
    // Handle empty or invalid discount code
    if (!discountCode || typeof discountCode !== 'string') {
        return total;
    }
    
    let discount = 0;
    
    if (discountCode === 'SAVE10') {
        discount = total * 0.1;
    } else if (discountCode === 'SAVE20') {
        discount = total * 0.2;
    } else if (discountCode === 'SAVE50') {
        // Fixed: Changed from 0.05 (5%) to 0.5 (50%)
        discount = total * 0.5;
    }
    
    // Fixed: Round to 2 decimal places to avoid floating-point precision issues
    return Math.round((total - discount) * 100) / 100;
}

/**
 * Calculate shipping cost based on cart weight
 * @param {Array} items - Array of item objects with weight and quantity
 * @returns {number} Shipping cost
 */
function calculateShipping(items) {
    // Handle empty cart
    if (!items || items.length === 0) {
        return 0;
    }
    
    let totalWeight = 0;
    
    for (let i = 0; i < items.length; i++) {
        // Validate weight exists and is a number
        if (typeof items[i].weight !== 'number') {
            throw new Error(`Invalid weight at index ${i}: must be a number`);
        }
        // Reject negative weight
        if (items[i].weight < 0) {
            throw new Error(`Invalid weight at index ${i}: cannot be negative`);
        }
        totalWeight += items[i].weight * items[i].quantity;
    }
    
    // Validate total weight is not negative
    if (totalWeight < 0) {
        throw new Error('Total weight cannot be negative');
    }
    
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
    
    // Validate inputs
    if (!items || items.length === 0) {
        return [];
    }
    if (!inventory || !Array.isArray(inventory)) {
        // If no inventory data, assume all items are out of stock
        return items.map(item => item.name);
    }
    
    // Optimized: Convert inventory to Map for O(1) lookup instead of O(n*m)
    const inventoryMap = new Map();
    for (let i = 0; i < inventory.length; i++) {
        inventoryMap.set(inventory[i].id, inventory[i]);
    }
    
    for (let i = 0; i < items.length; i++) {
        // Fixed: Use strict equality (===) instead of loose equality (==)
        const inventoryItem = inventoryMap.get(items[i].id);
        
        // Fixed: Handle case when item not found in inventory
        if (!inventoryItem) {
            outOfStock.push(items[i].name);
            continue;
        }
        
        if (inventoryItem.stock < items[i].quantity) {
            outOfStock.push(items[i].name);
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
    // Validate input type
    if (typeof amount !== 'number' || isNaN(amount)) {
        throw new Error('Invalid amount: must be a number');
    }
    // Fixed: Round to 2 decimal places first to avoid floating-point display issues
    const rounded = Math.round(amount * 100) / 100;
    return '$' + rounded.toFixed(2);
}

/**
 * Main cart calculator
 * @param {Object} cart - Cart object with items and discount code
 * @param {Array} inventory - Inventory data
 * @returns {Object} Cart summary with totals
 */
function calculateCartTotal(cart, inventory) {
    // Validate cart structure
    if (!cart || !Array.isArray(cart.items)) {
        throw new Error('Invalid cart: must have items array');
    }
    
    const subtotal = calculateSubtotal(cart.items);
    const discounted = applyDiscount(subtotal, cart.discountCode);
    const shipping = calculateShipping(cart.items);
    const outOfStockItems = checkStock(cart.items, inventory);
    
    // Fixed: Round total to avoid floating-point precision issues
    const total = Math.round((discounted + shipping) * 100) / 100;
    
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

// Export functions for testing
module.exports = {
    calculateSubtotal,
    applyDiscount,
    calculateShipping,
    checkStock,
    formatCurrency,
    calculateCartTotal
};
