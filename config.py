from notion.client import NotionClient

class global_var:

    # 请手动通过浏览器记录的 cookies 获取 token并填入
    client = NotionClient(token_v2="v02%3Auser_token_or_cookies%3ArY1ppkDr7NXH6sLIRmljOU-wbqdUuEZ8Oy")
    # 请手动设置表格的 Url 
    tableUrl ="https://www.notion.so/g0f/59562b42875c4417af24a281c1c08d20?v=075707e7a03945d99739da0316d91c4e&pvs=4"
    

# Gui预留接口 用于修改设置
def set_client(client):
    global_var.client = client
def get_client():
    return global_var.client
