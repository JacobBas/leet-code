function uniquePaths(m, n) {
  let resp = 1;
  for (let i = 1; i < m + n - 1; i++) {
    resp *= i;
    i < n ? (resp /= i) : (resp /= i - n + 1);
  }
  return resp;
}
