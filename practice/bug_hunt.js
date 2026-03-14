/**
 * Debugging Practice: Bug Hunt Exercise
 * This file contains 5 intentional bugs for debugging practice.
 * Find and fix each issue!
 */

// Fixed Bug 1: Logic error in calculation
function calculateDiscount(price, discountPercent) {
  // Divide discountPercent by 100 to get the actual discount amount
  const discount = price * (discountPercent / 100);
  return price - discount;
}

// Fixed Bug 2: Missing edge case handling
function findMaxValue(numbers) {
  // Handle empty array edge case
  if (!numbers || numbers.length === 0) {
    return null;
  }
  let max = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  return max;
}

// Note: Linear search is O(n). For repeated lookups, consider using a Map for O(1) access.
function searchUser(users, targetId) {
  // For single lookups, linear search is acceptable
  for (let i = 0; i < users.length; i++) {
    if (users[i].id === targetId) {
      return users[i];
    }
  }
  return null;
}

// Fixed Bug 4: Async/await mistake
async function fetchUserData(userId) {
  // Properly await both fetch and json calls
  const response = await fetch(`/api/users/${userId}`);
  const data = await response.json();
  return data;
}

// Fixed Bug 5: Variable scope issue
function processItems(items) {
  const results = [];
  // Properly declare loop variable with let
  for (let i = 0; i < items.length; i++) {
    results.push(items[i] * 2);
  }
  return results;
}

// Export for testing
module.exports = {
  calculateDiscount,
  findMaxValue,
  searchUser,
  fetchUserData,
  processItems
};
