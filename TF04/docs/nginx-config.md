# Documentação da Configuração Nginx

## Visão Geral
O Nginx atua como load balancer e proxy reverso, distribuindo requisições entre 3 instâncias backend.

## Arquivos de Configuração

### nginx.conf
Configuração principal com:
- `worker_connections 1024`: Conexões simultâneas por worker
- `limit_req_zone`: Zonas de rate limiting (10r/s para API, 30r/s geral)
- `log_format upstream_log`: Log personalizado com info de upstream (addr, response_time, status)
- `gzip on`: Compressão habilitada para text/plain, CSS, JSON, JS, XML, HTML

### conf.d/load-balancer.conf
- `upstream backend_cluster`: Cluster com `least_conn` e 3 backends
- `max_fails=3 fail_timeout=30s`: Health check passivo — marca backend como down após 3 falhas
- `proxy_next_upstream`: Failover automático em caso de erro, timeout ou 5xx
- Locations: `/` (frontend), `/api/` (backend com rate limit), `/admin/`, `/health`, `/nginx-status`

### conf.d/ssl.conf
- SSL termination na porta 443 com certificado self-signed
- Protocolos TLSv1.2 e TLSv1.3
- Mesmas locations do HTTP, com header `X-Forwarded-Proto: https`

## Headers de Proxy
- `X-Real-IP`: IP original do cliente
- `X-Forwarded-For`: Cadeia de proxies
- `X-Forwarded-Proto`: Protocolo original (http/https)
- `Host`: Host original da requisição
