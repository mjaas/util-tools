import os

# 切り替えたいAWS環境の名前を入力
input_env = str.lower(input("What env are you going to use ? :"))

# 有効な環境名であれば環境変数に設定
if input_env == "dev":
    os.environ["AWS_ACCESS_KEY_ID"] = "hoge-dev"
    sec_key = "fuga-dev"
    os.environ["AWS_SECRET_ACCESS_KEY"] = sec_key
elif input_env == "stg":
    os.environ["AWS_ACCESS_KEY_ID"] = "hoge-stg"
    sec_key = "fuga-stg"
    os.environ["AWS_SECRET_ACCESS_KEY"] = sec_key
elif input_env == "prd":
    os.environ["AWS_ACCESS_KEY_ID"] = "hoge-prd"
    sec_key = "fuga-prd"
    os.environ["AWS_SECRET_ACCESS_KEY"] = sec_key
elif input_env == "ci-prd":
    os.environ["AWS_ACCESS_KEY_ID"] = "hoge-ci-prd"
    sec_key = "fuga-ci-prd"
    os.environ["AWS_SECRET_ACCESS_KEY"] = sec_key
else:
    print("Input env \"" + input_env + "\" is not available.")

# 有効な環境名を入力したらsetした環境変数を表示. SECRET_ACCESS_KEYは末尾4桁以外はマスクして表示.
if input_env in ["dev", "stg", "prd", "ci-prd"]:
    sec_key_masked = "*" * (len(sec_key)-3) + sec_key[-3:]
    print("AWS_ACCESS_KEY_ID: " + os.environ["AWS_ACCESS_KEY_ID"])
    print("AWS_SECRET_ACCESS_KEY: " + sec_key_masked)