function twoSum(nums, target) {
  let m = new Map();
  for (let i = 0; i < nums.length; i++) {
    let y = target - nums[i];
    if (m.has(y)) {
      return [m.get(y), i];
    }
    m.set(nums[i], i);
  }
}

let nums = [0, 3, 4, 5, 6];
let target = 6;
console.log(twoSum(nums, target));
