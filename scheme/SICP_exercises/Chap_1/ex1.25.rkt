#lang racket

(define (fermat-test n)
  (define (try-it a)
    ;; change to expmod-new
    (= (expmod-new a n n) a))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
  (cond ((= times 0) true)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else false)))


;; code snippet
;; compute base^exp mod m
(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder
          (square (expmod base (/ exp 2) m))
          m))
        (else
         (remainder
          (* base (expmod base (- exp 1) m))
          m))))

(define (expmod-new base exp m)
  (remainder (fast-expt base exp) m))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (even? n)
  (= (remainder n 2) 0))

(define (square x)
  (display "square ")(display x)(newline) 
  (* x x))

;; test
;(fast-prime? 131 10)
;(expmod-new 2 5 3)
(expmod 5 101 101)
(expmod-new 5 101 101)