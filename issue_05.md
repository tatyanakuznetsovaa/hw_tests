### Запустить тесты

```
python3 -m unittest -v issue_05.py
test_what_is_year_now_error_format (issue_05.TestWhatIsYearNow.test_what_is_year_now_error_format) ... ok
test_what_is_year_now_format_1 (issue_05.TestWhatIsYearNow.test_what_is_year_now_format_1) ... ok
test_what_is_year_now_format_2 (issue_05.TestWhatIsYearNow.test_what_is_year_now_format_2) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

### Сгенерировать coverage report
```
python3 -m pytest -q issue_05.py --cov=what_is_year_now --cov-report html
...                                                                                                                                                  [100%]

---------- coverage: platform darwin, python 3.12.0-final-0 ----------
Coverage HTML written to dir htmlcov
```