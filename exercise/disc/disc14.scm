(define (deep-map fn lst)
		(cond ((eq? lst nil) nil)
			  ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
			  (else (cons (fn (car lst)) (deep-map fn (cdr lst))))
		
		)
)

