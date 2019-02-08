const reduce = require('./reduce');

test('empty list returns null', () => {
    const [result, step] = reduce([]);
    expect(result).toBe(null);
    expect(step).toBe(null);
});

test('single element list returns immediately', () => {
    const [result, step] = reduce([1]);
    expect(result).toBe(1);
    expect(step).toBe(0);
});

test('two elements list adds in one step', () => {
    const [result, step] = reduce([1, 2]);
    expect(result).toBe(3);
    expect(step).toBe(1);
});

test('odd length arrays can be summed', () => {
    const [result, step] = reduce([33, 6, 9, 1, 23, 88, 2]);
    expect(result).toBe(162);
    expect(step).toBe(3);
});

test('even length arrays can be summed', () => {
    const [result, step] = reduce([33, 6, 9, 1, 23, 88, 2, 123]);
    expect(result).toBe(285);
    expect(step).toBe(3);
});
