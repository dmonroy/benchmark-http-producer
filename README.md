# Benchmark HTTP Producer

How to execute the benchmark:

```
bash start_benchmark [Total requests] [Concurrent calls] [Gunicorn Workers]
```

So if we want to test a total of 100 http calls with 2 concurrent connections and using a single worker. This is the command to use:

```
bash start_benchmark 100 2 1
```

Or better, execute an aggressive test:

```
bash start_benchmark 100000 500 4
```

Play with it!
