# Dimensionnement des ressources Kubernetes

## 1. Objectif

Définir les règles de gestion CPU et mémoire du projet :
Mise en œuvre dune architecture Kubernetes hautement disponible
avec stratégies de déploiement Blue-Green et Canary.

## 2. Environnement local

| Ressource | Configuration |
|---|---|
| RAM physique | 7,88 Go |
| Limite WSL2 | 4 Go |
| CPU WSL2 | 4 |
| Swap WSL2 | 2 Go |
| Cluster | Devops-memo |
| Control Plane | 1 |
| Workers | 0 |
| Kubernetes | K3s v1.35.5 |

## 3. Mesures observées

Dernier relevé du 11 novembre 2026 :

| Indicateur | Valeur |
|---|---:|
| Nœud | Ready |
| CPU utilisé | 185m |
| CPU utilisé (%) | 4 % |
| Mémoire du nœud | 955 Mi |
| Mémoire utilisée (%) | 24 % |
| RAM libre Windows | 1,01 Go |

## 4. Politique de ressources

Les applications devront déclarer des requests et limits.

Configuration initiale indicative :

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi
