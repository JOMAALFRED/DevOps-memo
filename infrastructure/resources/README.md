# Gestion des ressources Kubernetes

## Objectif

Ce répertoire regroupe les politiques et les règles
de dimensionnement des ressources du projet.

Projet :
Mise en œuvre dune architecture Kubernetes hautement disponible avec stratégies de déploiement Blue-Green et Canary.

## Organisation

| Fichier | Description |
|---|---|
| node-sizing.md | Dimensionnement et capacité des nœuds |
| resource-quota.yaml | Quotas globaux des namespaces |
| limit-range.yaml | Limites et valeurs par défaut des conteneurs |

## Principes

- Déclarer les requests et limits des applications.
- Contrôler la consommation CPU et mémoire.
- Éviter la saturation des nœuds.
- Adapter les quotas aux capacités disponibles.
- Mesurer les ressources avant chaque évolution.

## Application des politiques

Les fichiers YAML seront appliqués uniquement après
la définition des namespaces applicatifs et la validation
des valeurs de ressources.

Aucune politique ne doit perturber les composants système
du cluster Kubernetes.

## Environnement

Cluster local : Devops-memo
Distribution Kubernetes : K3s
Orchestrateur : Kubernetes
