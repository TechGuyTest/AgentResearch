/**
 * Debugging Practice: Bug Hunt Exercise
 * This file contains 5 intentional bugs for debugging practice.
 * Find and fix each issue!
 */

// Bug 1: Logic error in calculation
function calculateDiscount(price, discountPercent) {
  // HINT: What happens when discount is 50%?
  const discount = price * discountPercent;
  return price - discount;
}

// Bug 2: Missing edge case handling
function findMaxValue(numbers) {
  // HINT: What if the array is empty?
  let max = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  return max;
}

// Bug 3: Inefficient pattern - can you spot it?
function searchUser(users, targetId) {
  // HINT: There's a better way than looping every time
  for (let i = 0; i < users.length; i++) {
    if (users[i].id === targetId) {
      return users[i];
    }
  }
  return null;
}

// Bug 4: Async/await mistake
async function fetchUserData(userId) {
  // HINT: What's missing here?
  const response = fetch(`/api/users/${userId}`);
  const data = response.json();
  return data;
}

// Bug 5: Variable scope issue
function processItems(items) {
  const results = [];
  // HINT: Check the loop variable declaration
  for (i = 0; i < items.length; i++) {
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
