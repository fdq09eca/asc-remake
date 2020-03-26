---
permalink: /about/
# class: wide
title: "About ERC"
toc: true
toc_label: Economics Research Centre
toc_icon: "cog"
author_profile: true
author: Travis Ng
header:
  overlay_color: "#000000"
  overlay_image: assets/images/index-hero.jpg
  overlay_filter: 0.5
---

# The Centre

The Economic Research Centre was established in July 2010. The Centre originated from the upgrading of its predecessor, the Hong Kong and Asia-Pacific Economies Programme, which had been part of the Hong Kong Institute of Asia-Pacific Studies since its inception in 1990. The mission of the Centre is to promote research and stimulate policy discussions on economic issues involving Hong Kong, Greater China, and the Asia-Pacific region. The Centre holds international conferences, seminars, and forums on relevant topics.

Members of the Centre include reputable scholars of The Chinese University of Hong Kong and other universities. Many of them have served as advisors in the advisory committees of the government, heads of various academic organizations, and editors/editorial board members of international academic journals.

# Our People

||Name|Position
:--:|:--:|:--:
{% for people in site.data.authors %}
{%- assign person = people[1] -%}
<img src="{{person.avatar}}" alt="this is a placeholder image" width="80px" height="80px" style="border-radius: 10%;">|[{{ person.name }}](person.links[1].url)|{{ person.bio }}
{% endfor %}




<!-- # Research Programmes

## Economic Policy Programme

Programme Director: CK Law
{: .text-right}

The Economic Policy Programme focuses on economic policy issues involving Hong Kong, Greater China and Asia-Pacific. Current research projects cover industrial and competition policies of Hong Kong, and aviation and micro-small-medium enterprises (MSME) policies of Asia-Pacific.

## Financial Markets Programme

The Financial Markets Programme has as its objective the enhancement of the public’s understanding of the development of Asia-Pacific financial markets, with a focus on Greater China. The Programme spearheads quality research on the financial integration of the Greater China area, the interaction between financial markets and the economy, the status of Hong Kong as a world-class financial centre, asset pricing and risk management, the regulation and governance of financial institutions, and the internationalization of the renminbi.

Since its establishment, the Programme has held a public lecture on investment strategies and published more than ten academic research articles on stock market returns, the capital structure of Asian firms, and the effectiveness of different technical indicators.

## Programme for Economic Education

The aim of the Programme for Economic Education is to promote excellence in economic education, and to improve understanding of public policy issues from economic perspectives. The members of the Programme are scholars and experts in economics and education from the Department of Decision Sciences and Managerial Economics, the Faculty of Education, the Department of Economics, and the Centre for Learning Enhancement and Research.

## Trade and Development Programme

The Trade and Development Programme focuses on the causes and consequences of globalization on economic development, inequality, and social welfare. The aim of the Programme is to generate high-quality academic studies and policy reports on international trade and global capital flows, and their impact on labour markets, industrial structures, and economic development. It also emphasizes the rise of China as the world’s factory, and Hong Kong’s status as Asia’s trade centre, as well as policies and issues related to trade and economic growth. -->
