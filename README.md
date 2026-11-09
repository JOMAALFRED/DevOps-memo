# DevOps-memo

## Sujet du mémoire

**Conception et mise en œuvre d'une architecture Kubernetes hautement disponible intégrant les stratégies de déploiement Blue-Green et Canary pour garantir la continuité des services applicatifs.**

## Objectif général

Concevoir, mettre en œuvre et tester une architecture Kubernetes permettant d'améliorer la disponibilité des applications et de réduire les interruptions de service pendant les déploiements.

## Objectifs spécifiques

- Concevoir une architecture Kubernetes hautement disponible.
- Déployer une application conteneurisée.
- Mettre en œuvre les stratégies Blue-Green et Canary avec Argo Rollouts.
- Automatiser les déploiements avec une chaîne CI/CD et GitOps.
- Surveiller les applications et l'infrastructure avec Prometheus et Grafana.
- Sécuriser les images et les déploiements avec Trivy.
- Réaliser des tests de panne, de basculement et de récupération.

## Architecture du projet

Le projet distingue deux environnements indépendants :

- **SmartOne** : environnement de réalisation et de validation en entreprise.
- **Maison** : environnement personnel de développement et d'expérimentation.

Chaque environnement possède ses propres configurations d'infrastructure et de déploiement Kubernetes.

Le code source de l'application est organisé séparément afin de pouvoir être réutilisé dans les deux environnements.

> Important : une simulation Kubernetes sur une seule machine ne constitue pas une haute disponibilité physique réelle.

## Technologies envisagées

| Domaine | Technologies |
|---|---|
| Conteneurisation | Docker |
| Orchestration | Kubernetes / K3s |
| Répartition de charge | HAProxy |
| GitOps | Argo CD |
| Stratégies de déploiement | Argo Rollouts |
| CI/CD | GitHub Actions |
| Supervision | Prometheus et Grafana |
| Sécurité des images | Trivy |

## Structure principale

```text
DevOps-memo/
 applications/
    web-app/
 clusters/
    smartone/
       infrastructure/
       applications/
    maison/
        infrastructure/
        applications/
 argo-rollouts/
 argocd/
 ci-cd/
 deployments/
    blue-green/
    canary/
 docs/
    architecture/
    installation/
    blue-green/
    canary/
    haute-disponibilite/
    tests/
 infrastructure/
    haproxy/
    kubernetes/
    monitoring/
    networking/
 scripts/
```

## Auteur

Moustaki Joma Alfred
