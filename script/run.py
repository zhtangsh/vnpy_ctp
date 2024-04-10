import logging

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy_ctp import CtpGateway
from vnpy.trader.object import (
    TickData,
    OrderData,
    TradeData,
    PositionData,
    AccountData,
    ContractData,
    OrderRequest,
    CancelRequest,
    SubscribeRequest,
)

from vnpy.trader.constant import (
    Direction,
    Offset,
    Exchange,
    OrderType,
    Product,
    Status,
    OptionType
)


def logging_config():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)-8s %(message)s'
    )


def main():
    """主入口函数"""

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway)
    gateway = main_engine.get_gateway('CTP')
    default_setting: dict[str, str] = {
        "用户名": "224850",
        "密码": "CWNXV@ijbYb2Ape",
        "经纪商代码": "9999",
        "交易服务器": "180.168.146.187:10130",
        "行情服务器": "180.168.146.187:10131",
        "产品名称": "simnow_client_test",
        "授权编码": "0000000000000000"
    }
    gateway.connect(default_setting)
    # T2406
    req = SubscribeRequest('T2406', Exchange.CFFEX)
    gateway.subscribe(req)
    gateway.query_account()
    gateway.query_position()


if __name__ == "__main__":
    logging_config()
    main()
