from notion.client import NotionClient

class global_var:

    # 请手动通过浏览器记录的 cookies 获取 token并填入
    client = NotionClient(token_v2="v02%3Auser_token_or_cookies%3ArY1ppkDr7NXH6sLIRmljOU-wbqdUuEZ8Oyi3R8nW2Offa8ltsl-RVPtg18VLeXlVj3BLsKC8EROblyvh5bfZ8xAxzn6Jh_1GlAHbJWD0LHQc9oVaqSREICjePChKBkNZTNWE")
    # 请手动设置表格的 Url 
    tableUrl ="https://www.notion.so/g0f/9becad6f3e8b4aa7ae21e74b60e1bde4?v=2fdf818db5154bb2bd33a7e5203a0685&pvs=4"
    

# Gui预留接口 用于修改设置
def set_client(client):
    global_var.client = client
def get_client():
    return global_var.client
