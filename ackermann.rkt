#lang racket

(define (φ m n p)
  (cond ((= p 0) (+ m n))
        ((= n 0)
         (cond ((= p 1) 0)
               ((= p 2) 1)
               (else m)))
        (else (φ m (φ m (- n 1) p) (- p 1)))))

(define (A m n)
  (cond ((= m 0) (+ n 1))
        ((= n 0) (A (- m 1) 1))
        (else (A (- m 1) (A m (- n 1))))))