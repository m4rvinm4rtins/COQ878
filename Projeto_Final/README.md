# CO₂ em Hidratos sI — Estudo com MLFF e Ab Initio

Este repositório contém o fluxo de trabalho computacional e as ferramentas de análise utilizadas no estudo do CO₂ confinado em cavidades de hidrato de gás do tipo sI, combinando simulações de dinâmica molecular baseadas em *Machine Learning Force Fields* (MLFF) e cálculos *ab initio*.

## Visão Geral

O trabalho investiga o comportamento estrutural, energético e orientacional de moléculas de CO₂ confinadas em cavidades 5¹² de hidratos sI à 
temperatura de 260 K. As simulações de dinâmica molecular foram realizadas utilizando o framework MACE, seguidas por avaliações *ab initio* de 
energias e forças por meio de cálculos *single-point* com o VASP, empregadas para fins de validação.

Os principais aspectos abordados incluem:
- Dinâmica molecular baseada em MLFF utilizando *foundation models* do MACE
- Validação energética e de forças em relação a cálculos DFT (VASP)
- Análise das energias de interação e do deslocamento quadrático médio (MSD)
- Construção da paisagem de energia livre \(F(r,\theta)\)
- Comparação com resultados *ab initio* reportados na literatura

## Metodologia

- **Dinâmica Molecular:**  
  MACE (*Machine Learning for Atomic Cluster Expansion*)  
  Ensemble: NVT, T = 260 K, termostato de Langevin

- **Cálculos Ab Initio:**  
  VASP (DFT, funcional GGA-PBE, correção de dispersão D3)  
  Cálculos *single-point* SCF em frames selecionados das trajetórias de MD

## Estrutura do Repositório

O repositório está organizado de forma simples, contendo notebooks de simulação e análise, 
bem como arquivos de trajetória gerados durante as simulações de dinâmica molecular:
├── README.md
├── equilibracao_via_mace.ipynb
├── producao.ipynb
├── Vasp_Vs_Mace.ipynb
├── mace_md_sI_CO2_260-K.xyz
└── producao_mace_md_sI_CO2_260-K.xyz


### Descrição dos arquivos

- **README.md**  
  Documento descritivo do repositório, contendo a visão geral do trabalho, metodologia e organização dos arquivos.

- **equilibracao_via_mace.ipynb**  
  Notebook responsável pela etapa de equilibração do sistema utilizando dinâmica molecular baseada em *Machine Learning Force Fields* (MACE), no ensemble NVT a 260 K. E posterior
  análise com o arquivo de produção.

- **producao.ipynb**  
  Notebook da etapa de produção da dinâmica molecular com MACE, a partir da configuração equilibrada, utilizado para a coleta de dados estatísticos e estruturais.

- **Vasp_Vs_Mace.ipynb**  
  Notebook dedicado à comparação entre as energias e forças calculadas pelo MACE e aquelas obtidas por cálculos *ab initio* *single-point* com o VASP.

- **mace_md_sI_CO2_260-K.xyz**  
  Arquivo de trajetória gerado durante a etapa de equilibração da dinâmica molecular com MACE.

- **producao_mace_md_sI_CO2_260-K.xyz**  
  Arquivo de trajetória da etapa de produção da dinâmica molecular com MACE, contendo energias e forças associadas aos frames
  simulados e porsterior cálculo de energias e forças para análise comparativa.

