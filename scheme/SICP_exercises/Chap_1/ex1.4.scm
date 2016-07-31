#lang racket

;; to get a + |b|
;; if b > 0: a + b
;; else: a - b

(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

;; for test
(a-plus-abs-b 2 -3)