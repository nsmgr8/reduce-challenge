/**
 * Sum all the elements in an array by splitting it in half recursively
 * @param arr the input array
 * @param step the recursion step
 *
 * @returns [sum of elements, steps required]
 */
function reduce(arr, step = 0) {
    const q = Math.floor(arr.length / 2);
    const r = arr.length % 2;

    if (q === 0) {
        // single element in the array, we're done
        if (r === 0) {
            // empty array returns unknown value
            return [null, null];
        }
        return [arr[0], step];
    }

    // prepend zero to first part for odd length array
    const first = r === 0 ? arr.slice(0, q) : [0, ...arr.slice(0, q)];
    const second = arr.slice(q);

    const result = first.map((x, i) => x + second[i]);
    return reduce(result, step + 1);
}

module.exports = reduce;
