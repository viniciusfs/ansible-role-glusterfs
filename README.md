# GlusterFS

Role para instalação e configuração do GlusterFS para volumes replicados. 

Para utilização da role é necessário um grupo chamado `glusterfs` no
inventário. A *role* criará o volume GlusterFS replicado entre todos os
servidores do grupo `glusterfs`.

## Descrição das variáveis

Nome | Descrição | Tipo | Padrão | Obrigatória
-----|-----------|------|--------|------------
glusterfs_volumes | Lista com informações dos volumes a serem configurados e montados | Lista | `[]` | Sim

### Descrição das variáveis para `glusterfs_volumes`

Nome | Descrição | Tipo | Padrão | Obrigatória
-----|-----------|------|--------|------------
name | Nome do volume GlusterFS | String | None | Sim
brick_path | Caminho para configuração dos bricks utilizados | Path| None | Sim
mount_point | Caminho para o ponto de montagem | Path | None | Sim

## Playbook de exemplo

Criação de um volume GlusterFS com nome `shared`, utilizando o brick
`/glusterfs/brick0` montado como `/shared` em todos servidores do grupo.

```yaml
---
- hosts: glusterfs
  vars:
    glusterfs_volumes:
    - name: shared
      brick_path: /glusterfs/brick0
      mount_point: /shared

  roles:
    - glusterfs
```
