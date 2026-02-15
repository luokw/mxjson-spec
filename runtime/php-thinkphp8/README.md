# MxJSON PHP Runtime (ThinkPHP 8)

> MxJSON 协议的 PHP 运行时引擎实现

## 状态

🚧 **开发中** - 完整引擎即将发布

## 计划功能

- [x] 协议解析器
- [x] 模型适配器（OpenAI/Claude）
- [x] 工作流调度器
- [ ] 人工审核节点
- [ ] 审计日志
- [ ] 动态UI渲染

## 安装

```bash
composer require mxjson/runtime-php
```

## 基本使用

```php
use MxJSON\Runtime;

$runtime = new Runtime([
    'openai_api_key' => 'sk-xxx',
]);

$result = $runtime->execute('path/to/capability.mxjson', [
    'input1' => 'value1',
]);
```

## 商业授权

企业私有化部署和高并发版本需要商业授权。

联系邮箱：luokongwei@gmail.com

## License

MIT (开源轻量版)
