(define (factorial x)
	(if (equal? x 1) x (* x (factorial (- x 1))))
)

(define (fib n)
	(cond ((= n 0) 0)
		  ((= n 1) 1)
		  (else (+ (fib (- n 1)) (fib (- n 2))))
	)
)

(define (my-append a b)
	(cond ((eq? b nil) nil)
		  ((eq? a nil) (cons (car b) (my-append a (cdr b))))
		  (else (cons (car a) (my-append (cdr a) b)))
	)
)

(define (duplicate lst)
		(cond ((eq? lst nil) nil)
			  (else (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
			  )
		)
)


(define (insert element lst index)
		(cond ((= index 0) (cons element (insert element lst (- index 1))))
			  ((eq? lst nil) nil)
			  (else (cons (car lst) (insert element (cdr lst) (- index 1)))
			  )

		)
)
; 这里index从0开始，index=0表明在lst的第一个前插入element

