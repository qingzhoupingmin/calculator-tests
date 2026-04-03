# ====================================
# 计算器测试项目 Dockerfile
# ====================================

# 第1步：选择基础镜像
# python:3.9-slim - Python 3.9的轻量级版本
FROM python:3.9-slim

# 第2步：设置工作目录
# WORKDIR指令设置容器内的工作目录
# 所有后续命令都在这个目录下执行
WORKDIR /app/tests

# 第3步：设置环境变量
# 避免Python生成.pyc文件
# 避免缓冲输出
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 第4步：复制依赖文件
# 先复制requirement.txt，利用Docker缓存层
# 只有requirement.txt变化时才重新安装依赖
COPY requirement.txt .

# 第5步：安装依赖
# 使用pip安装requirements.txt中的包
# --no-cache-dir 减小镜像体积
RUN pip install --no-cache-dir -r requirement.txt

# 第6步：复制项目文件
# 复制所有测试代码到容器中
COPY . .

# 第7步：设置Python路径
# 让Python能够找到calculator包
ENV PYTHONPATH=/app:$PYTHONPATH

# 第8步：显示Python路径（用于调试）
RUN echo "Python路径: $PYTHONPATH" && \
    echo "当前目录: $(pwd)" && \
    echo "文件列表:" && \
    ls -la && \
    echo "上级目录内容:" && \
    ls -la /app/

# 第9步：默认命令
# 容器启动时运行的默认命令
CMD ["pytest", "-v"]
