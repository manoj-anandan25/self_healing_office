# Runbook: DNS Failure

## Symptoms
- Users report "cannot resolve host"
- nslookup returns "Non-existent domain"
- Applications fail to connect

## Steps
1. Verify DNS server reachability (ping).
2. Check DNS service status and logs.
3. Flush client DNS cache.
4. Switch to backup DNS server.
5. Escalate if persistent across multiple servers.