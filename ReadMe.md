1. activate the venv

`source venv/bin/activate`

2.

```shell
export FLASK_APP=main.py
export FLASK_ENV=development
```

3.  ` flask run`

4.  Try with these

```shell
curl -X POST http://localhost:5000/translate \
-H "Content-Type: application/json" \
-d '{"text": "咁都係果啲嘢㗎啦，廿鯪蚊個餐又湯又剩唔通有得你食天九翅咩？求求其其有啲肉有啲菜蛋白質澱粉質撈撈埋埋打個白汁茄汁黑椒汁咁撐得你懵口懵面咪纍返去返工返學返廠返寫字樓囉。唔係你估真係搵餐晏仔咁簡單啊。咁跟飯定跟意粉啊？"}'

```
