(require :uiop)

(defparameter *s* (uiop:read-file-string  "../data/6.in" ))

(defun has-dup (ss)
    (string= (remove-duplicates ss) ss)
)

(defun marker-check (window)
    (loop for x from 0 to (- (length *s*) window)
        until (has-dup (subseq *s* x (+ x window)))
        maximize (+ x window 1)
    )
)

(format T "part 1: ~d~%" (marker-check 4))
(format T "part 2: ~d~%" (marker-check 14))
