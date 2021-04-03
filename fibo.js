const {
    performance
  } = require('perf_hooks');
  
  
  function fib(n) {
    if (n === 1 || n === 0) {
      return 1;
    }
    return fib(n - 1) + fib(n - 2);
  }

  function fibo2(nterms){
    let n1 = 0;
    let n2 = 1;
    count = 0
    while (count < nterms){
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
    }
    return n2
  }
  // fib(35);
  // console.log(fib(5) === fibo2(5))
  const t0 = performance.now();
  fibo(35);
  const t1 = performance.now();
  console.log(`${t1 - t0} ms`);
