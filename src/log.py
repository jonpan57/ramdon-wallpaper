from loguru import logger


def test():
    logger.add('logs/file.log')
    logger.debug("这是一个debug日志2")
    logger.info("这是一条info日志2")
