# Documentação de Load Balancing

## Algoritmo Utilizado: least_conn
Direciona cada nova requisição para o backend com menos conexões ativas. Ideal quando as requisições têm tempos de resposta variáveis.

## Instâncias
| Instância | Container | Porta Interna |
|-----------|-----------|---------------|
| Backend 1 | ecommerce-backend1 | 5000 |
| Backend 2 | ecommerce-backend2 | 5000 |
| Backend 3 | ecommerce-backend3 | 5000 |

## Health Checks
Configuração passiva: `max_fails=3 fail_timeout=30s`
- Após 3 falhas consecutivas, o backend é marcado como indisponível por 30 segundos
- Após o timeout, o Nginx tenta novamente automaticamente

## Failover
`proxy_next_upstream error timeout http_500 http_502 http_503`
- Se um backend falhar, a requisição é automaticamente redirecionada para outro backend saudável

## Rate Limiting
- API (`/api/`): 10 requisições/segundo com burst de 20
- Frontend: 30 requisições/segundo com burst de 20

## Testando o Balanceamento
```bash
# Ver distribuição entre instâncias
for i in {1..10}; do curl -s http://localhost/api/info | python3 -m json.tool; done

# Simular falha
docker stop ecommerce-backend1
curl http://localhost/api/info  # Deve responder via backend2 ou backend3

# Restaurar
docker start ecommerce-backend1
```

## Monitoramento
- `http://localhost/nginx-status` — Métricas do Nginx (conexões ativas, aceitas, etc.)
- `http://localhost/health` — Health check do load balancer
- Logs: `docker-compose logs nginx` — Inclui upstream_addr e upstream_response_time
