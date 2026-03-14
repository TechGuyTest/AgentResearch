/**
 * Unit Tests for Bug Hunt Exercise
 * These tests expose the 5 intentional bugs in bug_hunt.js
 */

const assert = require('assert');
const {
  calculateDiscount,
  findMaxValue,
  searchUser,
  fetchUserData,
  processItems
} = require('./bug_hunt');

describe('calculateDiscount', () => {
  it('should calculate 50% discount correctly', () => {
    // Bug: Currently returns -4900 instead of 50
    // price=100, discountPercent=50 should mean 50% off = 50
    const result = calculateDiscount(100, 50);
    assert.strictEqual(result, 50, '50% discount on 100 should be 50');
  });

  it('should calculate 20% discount correctly', () => {
    // Bug: Currently returns 80 instead of 80... wait, 100 * 20 = 2000, 100 - 2000 = -1900
    const result = calculateDiscount(100, 20);
    assert.strictEqual(result, 80, '20% discount on 100 should be 80');
  });

  it('should calculate 0% discount correctly', () => {
    const result = calculateDiscount(100, 0);
    assert.strictEqual(result, 100, '0% discount on 100 should be 100');
  });

  it('should calculate 100% discount correctly', () => {
    const result = calculateDiscount(100, 100);
    assert.strictEqual(result, 0, '100% discount on 100 should be 0');
  });
});

describe('findMaxValue', () => {
  it('should find max in normal array', () => {
    const result = findMaxValue([1, 5, 3, 9, 2]);
    assert.strictEqual(result, 9);
  });

  it('should handle empty array', () => {
    // Bug: Currently returns undefined or throws error
    const result = findMaxValue([]);
    assert.strictEqual(result, null, 'Empty array should return null');
  });

  it('should handle single element array', () => {
    const result = findMaxValue([42]);
    assert.strictEqual(result, 42);
  });

  it('should handle negative numbers', () => {
    const result = findMaxValue([-5, -2, -10, -1]);
    assert.strictEqual(result, -1);
  });
});

describe('searchUser', () => {
  it('should find user by id', () => {
    const users = [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' },
      { id: 3, name: 'Charlie' }
    ];
    const result = searchUser(users, 2);
    assert.deepStrictEqual(result, { id: 2, name: 'Bob' });
  });

  it('should return null for non-existent user', () => {
    const users = [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' }
    ];
    const result = searchUser(users, 999);
    assert.strictEqual(result, null);
  });

  it('should handle empty users array', () => {
    const result = searchUser([], 1);
    assert.strictEqual(result, null);
  });
});

describe('fetchUserData', () => {
  it('should properly await fetch and json calls', async () => {
    // Bug: Missing await keywords cause Promise objects to be returned instead of data
    // This test will fail with current implementation
    global.fetch = async (url) => ({
      json: async () => ({ id: 1, name: 'Test User' })
    });
    
    const result = await fetchUserData(1);
    assert.deepStrictEqual(result, { id: 1, name: 'Test User' });
    assert.notStrictEqual(typeof result.then, 'function', 'Should return resolved data, not a Promise');
  });
});

describe('processItems', () => {
  it('should process items correctly', () => {
    const result = processItems([1, 2, 3]);
    assert.deepStrictEqual(result, [2, 4, 6]);
  });

  it('should not pollute global scope with loop variable', () => {
    // Bug: Loop variable 'i' is not declared, polluting global scope
    const globalIBefore = global.i;
    processItems([1, 2, 3]);
    const globalIAfter = global.i;
    
    // In strict mode or proper implementation, global.i should be undefined
    // In non-strict mode with bug, global.i will be 3
    assert.strictEqual(globalIAfter, undefined, 'Loop variable should not pollute global scope');
    
    // Cleanup if it was set
    if (globalIAfter !== undefined) {
      delete global.i;
    }
  });

  it('should handle empty array', () => {
    const result = processItems([]);
    assert.deepStrictEqual(result, []);
  });
});
