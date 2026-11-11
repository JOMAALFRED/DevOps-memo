# Dimensionnement des ressources Kubernetes

## 1. Objectif

Ce document définit les règles de dimensionnement des ressources CPU et mémoire pour le projet :

** Mise en œuvre dune architecture Kubernetes hautement disponible avec stratégies de déploiement Blue-Green et Canary **

L'objectif est de garantir une utilisation maîtrisée des ressources pendant les expérimentations et les tests.

## 2. Environnement local actuel

| Ressource | Configuration |
|---|---|
| Mémoire physique Windows | 7,88 Go |
| Mémoire maximale WSL2 | 4 Go |
| Processeurs WSL2 | 4 |
| Swap WSL2 | 2 Go |
| Docker Desktop | Environ 4 Go |
| Cluster k3d | Devops-memo |
| Nœuds Control Plane | 1 |
| Nœuds Worker | 0 |
| Kubernetes | K3s v1.35.5 |

**Attention :** les limites WSL2 et Docker représentent des plafonds de ressources et non des réservations indépendantes. Elles ne doivent pas être additionnées.

## 3. État observé du cluster

Dernier relevé disponible du 11 novembre 2026 :

| Indicateur | Valeur |
|---|---:|
| État du nœud | Ready |
| CPU utilisé | 216m (5 %) |
| Mémoire du nœud | 980 Mi (25 %) |
| RAM libre Windows | 1,01 Go |
| Nombre de Workers | 0 |

Ces valeurs sont des mesures ponctuelles et peuvent évoluer. Elles doivent être relevées à nouveau lors des expérimentations.

La mémoire mesurée au niveau du nœud comprend davantage que la somme des consommations des Pods.

## 4. Politique de dimensionnement

### 4.1 Nœuds Kubernetes

Le Control Plane actuel ne doit pas recevoir une limite mémoire Docker stricte de 1 Go sans étude préalable.

Le nœud utilise déjà environ 950 MiB selon les mesures Docker précédentes. Une limite trop proche de cette consommation pourrait provoquer un arrêt OOM.

L'ajout d'un Worker sera étudié uniquement après vérification de la mémoire disponible et de la stabilité de Docker Desktop.

### 4.2 Applications

Configuration initiale recommandée pour une application légère :

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi
```

Les valeurs `requests` servent au placement des Pods par Kubernetes. Les valeurs `limits` définissent les plafonds de consommation des conteneurs.

### 4.3 ResourceQuota

Le namespace `memo-saas` dispose des limites globales suivantes :

| Ressource | Valeur maximale |
|---|---:|
| CPU requests | 500m |
| CPU limits | 1 |
| Mémoire requests | 512Mi |
| Mémoire limits | 1Gi |
| Nombre de Pods | 10 |

### 4.4 LimitRange

Les valeurs par défaut et les limites par conteneur sont :

| Paramètre | CPU | Mémoire |
|---|---:|---:|
| Request par défaut | 100m | 128Mi |
| Limit par défaut | 500m | 256Mi |
| Minimum | 50m | 64Mi |
| Maximum | 500m | 512Mi |

Ces politiques ont été appliquées et testées dans le namespace `memo-saas`.

## 5. Suivi et évolution

Avant d'augmenter le nombre de nœuds ou d'installer des composants de supervision supplémentaires, il faut vérifier :

- la mémoire disponible sur Windows ;
- la consommation du nœud Kubernetes ;
- l'état Ready des nœuds ;
- l'absence de condition MemoryPressure ;
- la stabilité des composants Docker et Kubernetes.

Les choix de dimensionnement seront réévalués à partir des mesures réalisées pendant les tests du projet.
