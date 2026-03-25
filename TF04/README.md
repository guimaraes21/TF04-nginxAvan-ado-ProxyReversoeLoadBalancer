# TF04 - E-commerce com Load Balancer Avançado

## Aluno
- **Nome:** Vitor Pinheiro Guimarães
- **RA:** 6324680
- **Curso:** Análise e Desenvolvimento de Sistemas

## Arquitetura
- **Nginx:** Load balancer com SSL e rate limiting
- **Backend:** 3 instâncias da API para alta disponibilidade
- **Frontend:** Loja virtual estática
- **Admin:** Painel administrativo

## Funcionalidades Implementadas
- ✅ Load balancing com algoritmo least_conn
- ✅ Health checks automáticos
- ✅ Failover transparente
- ✅ SSL/TLS com certificado self-signed
- ✅ Rate limiting para proteção
- ✅ Logs detalhados com upstream info
- ✅ Compressão gzip
- ✅ Virtual hosts

## Como Executar

### Pré-requisitos
- Docker e Docker Compose

### Execução
```bash
git clone [URL_DO_SEU_REPO]
cd TF04

# Gerar certificados SSL
bash scripts/generate-ssl.sh

# Subir todos os serviços
docker-compose up -d --build

# Verificar status
docker-compose ps
```

## Endpoints
- Frontend: http://localhost ou https://localhost
- API: http://localhost/api/
- Admin: http://localhost/admin/
- Status: http://localhost/nginx-status
- Health: http://localhost/health

## Testes de Load Balancing
```bash
# Testar distribuição de carga
for i in {1..10}; do
  curl -s http://localhost/api/info | python3 -m json.tool
done

# Simular falha de instância
docker stop ecommerce-backend1

# Verificar failover
curl http://localhost/api/info
```

## Monitoramento
- Logs detalhados: `docker-compose logs nginx`
- Métricas: http://localhost/nginx-status
- Health checks automáticos a cada 30s

## Validação
```bash
# Teste de load balancing
docker-compose up -d --build
for i in {1..6}; do curl -s http://localhost/api/info; done
docker-compose down
```
