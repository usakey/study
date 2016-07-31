#lang racket

;; product <- product * counter
;; counter <- counter + 1

(define (factorial n)
  (define (iter product counter)
    (if (> counter n)
        product
        (iter (* product counter)
              (+ counter 1))))
  (iter 1 1))

;; test
(factorial 5)