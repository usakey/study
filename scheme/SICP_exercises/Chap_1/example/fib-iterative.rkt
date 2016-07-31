#lang racket

(define (fib n)
  (define (fib-iter a b cnt)
    (if (= cnt 0)
        a
        (fib-iter b (+ a b) (- cnt 1))))
  (fib-iter 0 1 n)
  )

(fib 8)