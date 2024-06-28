// Do not submit class ListNode

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  let root = new ListNode();
  let l0 = root;
  let carry = 0;

  while (true) {
    const sum = (l1?.val || 0) + (l2?.val || 0) + carry;
    l0.val = sum % 10;
    carry = Math.floor(sum / 10);

    l1 = l1?.next || null;
    l2 = l2?.next || null;
    if (l1 || l2 || carry) {
      l0.next = new ListNode();
      l0 = l0.next;
    } else {
      break;
    }
  }

  return root;
}
