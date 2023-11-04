```
python3 -m unittest issue_03                                            
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

python3 -m unittest -v issue_03                         
test_fit_transform_default_case (issue_03.TestFitTransform.test_fit_transform_default_case) ... ok
test_fit_transform_empty_case (issue_03.TestFitTransform.test_fit_transform_empty_case) ... ok
test_fit_transform_noniter_args_bad_seq (issue_03.TestFitTransform.test_fit_transform_noniter_args_bad_seq) ... ok
test_fit_transform_noniter_args_good_seq (issue_03.TestFitTransform.test_fit_transform_noniter_args_good_seq) ... ok
test_fit_transform_wo_args (issue_03.TestFitTransform.test_fit_transform_wo_args) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK


python3 -m unittest issue_03.TestFitTransform.test_fit_transform_wo_args
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


python3 -m unittest -v issue_03 -k fit_transform_noniter
test_fit_transform_noniter_args_bad_seq (issue_03.TestFitTransform.test_fit_transform_noniter_args_bad_seq) ... ok
test_fit_transform_noniter_args_good_seq (issue_03.TestFitTransform.test_fit_transform_noniter_args_good_seq) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```