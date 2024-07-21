// This is a O((m+n)/2) solution. It's a bit trickier to code the O(log(m+n)) version.

function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const totalLength = nums1.length + nums2.length;
  const halfLength = Math.floor(totalLength / 2);
  // Handle even and odd lengths to indexes: 20 -> 9, 10; 21 -> 10, 10
  const [targetIndex1, targetIndex2] = [
    totalLength % 2 === 0 ? halfLength - 1 : halfLength,
    halfLength,
  ];

  const arr: number[] = [];
  let p1 = 0,
    p2 = 0,
    n1 = 0,
    n2 = 0;
  while (p1 < nums1.length && p2 < nums2.length) {
    n1 = nums1[p1];
    n2 = nums2[p2];
    if (n1 <= n2) {
      arr.push(n1);
      p1 += 1;
    } else {
      arr.push(n2);
      p2 += 1;
    }

    if (arr.length > targetIndex2) {
      return (arr[targetIndex1] + arr[targetIndex2]) / 2;
    }
  }

  if (p1 === nums1.length) {
    arr.push(...nums2.slice(p2));
  } else if (p2 === nums2.length) {
    arr.push(...nums1.slice(p1));
  }
  return (arr[targetIndex1] + arr[targetIndex2]) / 2;
}
