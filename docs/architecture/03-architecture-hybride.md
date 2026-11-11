\# 03 — Architecture hybride



\## 1. Introduction



Dans le cadre de ce projet, nous adoptons une approche hybride qui distingue l'architecture cible professionnelle de l'environnement de laboratoire utilisé pour les expérimentations.



Cette séparation permet de concevoir une infrastructure Kubernetes hautement disponible tout en réalisant les démonstrations pratiques avec des ressources matérielles plus accessibles.



L'objectif est de mettre en œuvre des stratégies de déploiement Blue-Green et Canary afin de réduire les interruptions de service lors des mises à jour applicatives.



\## 2. Présentation de l'approche hybride



L'architecture hybride repose sur deux environnements complémentaires :



\- Une architecture cible professionnelle, destinée à représenter une infrastructure Kubernetes hautement disponible.

\- Un laboratoire virtuel, destiné à réaliser les installations, configurations et expérimentations pratiques.



Ces deux environnements partagent les mêmes principes techniques, mais ne possèdent pas nécessairement les mêmes capacités matérielles.



\## 3. Architecture cible professionnelle



\### 3.1 Composants principaux



L'architecture cible prévoit les composants suivants :



| Composant | Quantité minimale prévue | Fonction |

|---|---:|---|

| Nœuds Control Plane | 3 | Gestion du cluster Kubernetes et quorum etcd |

| Nœuds Worker | 2 | Exécution des applications |

| Load Balancers | 2 | Répartition et disponibilité du point d'entrée |

| Stockage persistant | Selon la solution retenue | Conservation des données applicatives |

| Serveur ou plateforme de supervision | Selon dimensionnement | Collecte et visualisation des métriques |



\### 3.2 Haute disponibilité



Les trois nœuds Control Plane permettent de maintenir un quorum etcd de deux membres sur trois.



Cette configuration permet de tolérer la perte d'un membre etcd sans perdre le quorum, sous réserve du bon fonctionnement des autres composants.



Les deux Workers permettent de répartir les applications sur plusieurs nœuds.



Les Load Balancers sont prévus en redondance afin d'éviter qu'un seul point d'entrée constitue un point de défaillance unique.



La véritable haute disponibilité nécessite que les composants soient répartis sur des machines physiques ou des domaines de défaillance indépendants.



\## 4. Laboratoire virtuel de démonstration



\### 4.1 Objectif



Le laboratoire virtuel permet de reproduire les principales fonctionnalités de l'architecture cible dans un environnement contrôlé.



Il sera utilisé pour :



\- Installer et configurer Kubernetes.

\- Déployer une application conteneurisée.

\- Mettre en place une chaîne CI/CD.

\- Configurer Argo CD pour le GitOps.

\- Installer Argo Rollouts.

\- Expérimenter les stratégies Blue-Green et Canary.

\- Mettre en place Prometheus et Grafana.

\- Réaliser des tests de fonctionnement et de résilience.



\### 4.2 Composants logiciels



| Technologie | Utilisation |

|---|---|

| Docker | Conteneurisation |

| Kubernetes | Orchestration |

| GitHub | Gestion du code et des configurations |

| GitHub Actions ou GitLab CI | Intégration continue |

| Argo CD | Déploiement GitOps |

| Argo Rollouts | Stratégies Blue-Green et Canary |

| HAProxy | Répartition du trafic |

| Prometheus | Collecte des métriques |

| Grafana | Visualisation et supervision |

| Trivy | Analyse de sécurité des images |



Les technologies définitives seront confirmées pendant la phase d'implémentation.



\## 5. Comparaison des deux environnements



| Critère | Architecture cible | Laboratoire |

|---|---|---|

| Objectif | Haute disponibilité professionnelle | Expérimentation |

| Infrastructure | Machines indépendantes | Machines virtuelles ou cluster local |

| Control Plane | 3 nœuds | Selon les ressources disponibles |

| Workers | 2 minimum | Selon les ressources disponibles |

| GitOps | Prévu | Mis en œuvre et testé |

| Blue-Green | Prévu | Démontré |

| Canary | Prévu | Démontré |

| Tests de panne | Validation de conception et tests réels | Simulation contrôlée |



\## 6. Limites et précautions



Un cluster composé de plusieurs machines virtuelles exécutées sur un seul ordinateur ne garantit pas une haute disponibilité physique.



En cas de panne de l'ordinateur hôte, toutes les machines virtuelles peuvent devenir indisponibles.



De même, la disponibilité de l'application dépend du réseau, du stockage, des points d'entrée et des autres composants de l'infrastructure.



Les résultats obtenus dans le laboratoire devront donc être présentés comme des résultats expérimentaux et non comme une preuve de haute disponibilité physique.



\## 7. Conclusion



L'approche hybride permet de concilier la conception d'une architecture Kubernetes professionnelle et la réalisation de démonstrations pratiques dans un laboratoire accessible.



Elle constitue le cadre de référence pour les prochaines étapes du projet, notamment la mise en place de Kubernetes, l'automatisation CI/CD, GitOps, Blue-Green, Canary et la supervision.
