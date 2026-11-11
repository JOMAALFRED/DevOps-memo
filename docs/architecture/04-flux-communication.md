\# 04 — Flux de communication de l'architecture



\## 1. Introduction



Cette documentation présente les principaux flux de communication entre les composants de l'architecture Kubernetes hautement disponible.



L'objectif est d'identifier les communications nécessaires au fonctionnement du cluster, au déploiement des applications et à la supervision.



Les ports indiqués sont des valeurs de référence à confirmer selon les technologies et les configurations retenues.



\## 2. Flux du plan de contrôle Kubernetes



| Source | Destination | Protocole / Port | Fonction |

|---|---|---|---|

| Administrateur | API Server | TCP 6443 | Administration Kubernetes |

| Composants du Control Plane | etcd | TCP 2379 | Accès au magasin de données etcd |

| Membres etcd | Membres etcd | TCP 2380 | Communication entre membres etcd |

| Control Plane | Kubelet | TCP 10250 | Communication avec les nœuds |

| Kubelet | API Server | TCP 6443 | Communication avec le plan de contrôle |



\## 3. Flux applicatifs



| Source | Destination | Port | Fonction |

|---|---|---|---|

| Clients | Load Balancer | TCP 80 | Accès HTTP |

| Clients | Load Balancer | TCP 443 | Accès HTTPS |

| Load Balancer | Ingress Controller | Selon configuration | Transmission du trafic |

| Ingress Controller | Service Kubernetes | Port du Service | Routage vers l'application |

| Service Kubernetes | Pods | Port cible | Distribution vers les instances applicatives |



\## 4. Flux GitOps et CI/CD



| Source | Destination | Port | Fonction |

|---|---|---|---|

| Pipeline CI | Registre d'images | TCP 443 | Publication des images |

| Argo CD | Dépôt Git | TCP 443 ou SSH 22 | Récupération des manifestes |

| Argo CD | API Server | TCP 6443 | Synchronisation des ressources |

| Administrateur | Interface Argo CD | HTTPS | Administration GitOps |



\## 5. Flux de supervision



| Source | Destination | Port | Fonction |

|---|---|---|---|

| Prometheus | Exporters | Selon configuration | Collecte des métriques |

| Administrateur | Grafana | TCP 3000 par défaut | Consultation des tableaux de bord |

| Grafana | Prometheus | Selon configuration | Consultation des métriques |



\## 6. Principes de sécurité réseau



Les communications doivent respecter les principes suivants :



\- Autoriser uniquement les flux nécessaires.

\- Limiter l'accès à l'API Kubernetes aux administrateurs et composants autorisés.

\- Ne pas exposer directement etcd sur le réseau utilisateur.

\- Protéger les communications sensibles par TLS lorsque cela est applicable.

\- Restreindre l'accès aux interfaces d'administration.

\- Séparer les flux applicatifs, d'administration et de supervision lorsque l'infrastructure le permet.



\## 7. Précautions de mise en œuvre



Les ports présentés ne doivent pas être considérés comme des ports à ouvrir systématiquement sur le réseau physique.



Certains flux sont internes au cluster et sont gérés par Kubernetes, le CNI ou les composants concernés.



Les ports définitifs seront déterminés après le choix de la distribution Kubernetes, du CNI, de l'Ingress Controller et des outils de supervision.



Aucune modification du réseau physique de SmartOne n'est nécessaire pour rédiger cette conception.



\## 8. Conclusion



La définition des flux de communication permet de préparer une architecture cohérente, sécurisée et évolutive.



Elle servira de référence lors de l'installation et de la configuration des différents composants Kubernetes.
