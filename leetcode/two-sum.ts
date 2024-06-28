function twoSum(nums: number[], target: number): number[] {
  const ni = nums.map((n, i) => [n, i]).sort(([a], [b]) => a - b);

  let leftPointer = 0;
  let rightPointer = ni.length - 1;
  let total = 0;
  while (true) {
    total = ni[leftPointer][0] + ni[rightPointer][0];
    if (total > target) {
      rightPointer -= 1;
    } else if (total < target) {
      leftPointer += 1;
    } else {
      return [ni[leftPointer][1], ni[rightPointer][1]];
    }
  }
}
