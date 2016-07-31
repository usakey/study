#lang planet neil/sicp
;; add sicp package

(define (smallest-divisor n) (find-divisor n 2))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))

(define (square x)
  (* x x))

(define (divides? a b)
  (= (remainder b a) 0))

;; define prime
(define (prime? n)
  (= n (smallest-divisor n)))
;; above code snippets for prime test with O(n^(1/2))

(define (timed-prime-test n)
  (start-prime-test n (runtime)))

(define (start-prime-test n start-time)
  (if (prime? n)
      (report-prime n (- (runtime) start-time))
      #f))

(define (report-prime n elapsed-time)
  (newline)
  (display n)
  (display " *** ")
  (display elapsed-time)
  (newline))

;; todo
(define (even? n)
  (= (remainder n 2) 0))

(define (search-for-primes n cnt)
  (if (even? n)
      (sfp-iter (+ n 1) cnt)
      (sfp-iter n cnt)))

(define (sfp-iter n cnt)
  (if (> cnt 0)
      (if (timed-prime-test n)
          (sfp-iter (+ n 2) (- cnt 1))
          (sfp-iter (+ n 2) cnt))
      (display "***********")))

;; test
(search-for-primes 1000 3)
(search-for-primes 10000 3)
(search-for-primes 100000 3)
(search-for-primes 1000000 3)
(search-for-primes 10000000 3)
(search-for-primes 1000000000 3)
(search-for-primes 100000000000 3)
(search-for-primes 10000000000000 3)