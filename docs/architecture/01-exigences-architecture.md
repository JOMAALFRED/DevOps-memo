\# 01 — Exigences de l'architecture Kubernetes



\## 1. Contexte du projet



Ce projet consiste à concevoir et mettre en œuvre une architecture Kubernetes hautement disponible intégrant les stratégies de déploiement Blue-Green et Canary.



L'objectif est de garantir la continuité des services applicatifs, de réduire les interruptions pendant les mises à jour et d'améliorer la résilience de l'infrastructure.



\## 2. Objectif général



Mettre en place une architecture capable de maintenir les applications disponibles malgré certaines défaillances de composants et de permettre des déploiements progressifs et contrôlés.



\## 3. Exigences fonctionnelles



| Référence | Exigence |

|---|---|

| EF-01 | Déployer une application sous forme de conteneurs. |

| EF-02 | Orchestrer les conteneurs avec Kubernetes. |

| EF-03 | Disposer de plusieurs nœuds Control Plane. |

| EF-04 | Disposer de plusieurs nœuds Worker. |

| EF-05 | Répartir les requêtes avec une solution de Load Balancing. |

| EF-06 | Automatiser les déploiements avec une chaîne CI/CD. |

| EF-07 | Synchroniser les configurations Kubernetes depuis Git avec Argo CD. |

| EF-08 | Réaliser des déploiements Blue-Green avec Argo Rollouts. |

| EF-09 | Réaliser des déploiements Canary avec Argo Rollouts. |

| EF-10 | Superviser l'infrastructure et les applications avec Prometheus et Grafana. |

| EF-11 | Analyser les images de conteneurs avec Trivy. |

| EF-12 | Réaliser des tests de panne et de récupération. |



\## 4. Exigences non fonctionnelles



\### 4.1 Disponibilité



\- Éviter qu'une panne d'un seul nœud entraîne l'indisponibilité complète de l'application.

\- Prévoir plusieurs instances applicatives.

\- Éviter les points uniques de défaillance dans les composants critiques.

\- Prévoir un mécanisme de basculement en cas de panne.



\### 4.2 Résilience



\- Permettre la reprise des applications après une panne.

\- Vérifier le comportement du cluster après la perte d'un nœud.

\- Prévoir la surveillance de l'état des composants Kubernetes.



\### 4.3 Sécurité



\- Protéger les accès à l'API Kubernetes.

\- Séparer les configurations propres à chaque environnement.

\- Ne jamais versionner les mots de passe, tokens, clés privées ou autres secrets.

\- Analyser les images de conteneurs avant leur déploiement.



\### 4.4 Maintenabilité



\- Centraliser les configurations dans Git.

\- Documenter les procédures d'installation et d'exploitation.

\- Automatiser les opérations répétitives.

\- Faciliter le retour à une version applicative précédente.



\### 4.5 Supervision



\- Collecter les métriques des applications et de l'infrastructure.

\- Visualiser les indicateurs avec Grafana.

\- Détecter les anomalies et les dégradations de performances.



\## 5. Architecture cible envisagée



L'architecture cible prévoit :



\- Trois nœuds Control Plane pour assurer le quorum etcd.

\- Au moins deux nœuds Worker pour héberger les applications.

\- Une solution de Load Balancing avec HAProxy.

\- Un mécanisme de stockage adapté aux besoins de disponibilité.

\- Argo CD pour le GitOps.

\- Argo Rollouts pour les stratégies Blue-Green et Canary.

\- GitHub Actions pour la CI/CD.

\- Prometheus et Grafana pour la supervision.

\- Trivy pour l'analyse de sécurité des images.



Les nœuds devront être répartis sur des machines ou domaines de panne indépendants pour démontrer une véritable haute disponibilité physique.



\## 6. Indicateurs de disponibilité à définir



Les valeurs suivantes devront être définies et validées avant les tests :



| Indicateur | Signification | Valeur cible |

|---|---|---|

| SLA | Niveau de disponibilité du service | À définir |

| RTO | Durée maximale acceptable avant rétablissement | À définir |

| RPO | Perte maximale de données acceptable | À définir |

| Temps de déploiement | Durée d'une opération de déploiement | À mesurer |

| Temps de récupération | Durée nécessaire pour retrouver le service | À mesurer |



\## 7. Scénarios de validation



Les scénarios suivants seront étudiés :



1\. Déploiement initial de l'application.

2\. Mise à jour avec la stratégie Blue-Green.

3\. Mise à jour avec la stratégie Canary.

4\. Retour à la version précédente après une anomalie.

5\. Perte d'un nœud Worker.

6\. Perte d'un nœud Control Plane.

7\. Vérification du comportement du quorum etcd.

8\. Vérification de la supervision pendant une panne.

9\. Vérification de la reprise des services.



\## 8. Limites de la simulation



Une simulation comportant plusieurs nœuds Kubernetes sur une seule machine permet de tester les configurations et les mécanismes logiciels.



Cependant, elle ne démontre pas une véritable haute disponibilité physique : une panne de la machine hôte peut arrêter tous les nœuds virtuels ou conteneurisés.



La validation complète de la haute disponibilité nécessitera donc plusieurs machines ou domaines de panne indépendants.



\## 9. Conclusion



Ces exigences constituent la base de conception de l'architecture Kubernetes du projet.



Elles serviront à orienter les choix techniques, la configuration de l'infrastructure, les stratégies de déploiement et les scénarios de test.
