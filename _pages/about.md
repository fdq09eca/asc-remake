---
permalink: /about/
# class: wide
title: "About ERC"
# tagline: ""
toc: true
toc_label: Economics Research Centre
author_profile: true
# author: Travis Ng
header:
  overlay_color: "#000000"
  overlay_image: assets/images/erc-about.jpg
  overlay_filter: 0.5
sidebar:
  - title: ""
    text: <iframe src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FEconomic-Research-Centre-500334206838357%2F&tabs=timeline&width=250&height=300&small_header=true&adapt_container_width=true&hide_cover=true&show_facepile=true&appId" width="250" height="300" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allow="encrypted-media"></iframe>
---

# The Centre

The Economic Research Centre was established in July 2010. The Centre originated from the upgrading of its predecessor, the Hong Kong and Asia-Pacific Economies Programme, which had been part of the Hong Kong Institute of Asia-Pacific Studies since its inception in 1990. The mission of the Centre is to promote research and stimulate policy discussions on economic issues involving Hong Kong, Greater China, and the Asia-Pacific region. The Centre holds international conferences, seminars, and forums on relevant topics.
{: .text-justify}

Members of the Centre include reputable scholars of The Chinese University of Hong Kong and other universities. Many of them have served as advisors in the advisory committees of the government, heads of various academic organizations, and editors/editorial board members of international academic journals.
{: .text-justify}

# Our People

|     | Name | Position |
| :-: | :--: | :------: |
{% for people in site.data.authors %}
{%- assign person = people[1] -%}
![{{person.name}}]({{person.avatar | relative_url}}){: width="80px" height="80px" style="border-radius: 10%;"}|[{{ person.name }}]({{person.links[1].url}})|{{ person.bio }}
{% endfor %}

<!-- <img src="{{ person.avatar }}" alt="{{person.name}}" width="80px" height="80px" style="border-radius: 10%;"> -->
# Organisation
![org_chart](/assests/images/org_cht.jpg){: .align-center}

# Contact Us

<!-- <style>
    .google-maps {
        position: relative;
        padding-bottom: 75%; // This is the aspect ratio
        height: 0;
        overflow: hidden;
    }
    .google-maps iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100% !important;
        height: 100% !important;
    }
</style> -->

<div class="google-maps">
  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3688.4012620095523!2d114.2064284154815!3d22.413918144423786!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3404089dde4ca0f5%3A0xfe9175be16d897fb!2sEsther%20Lee%20Building%2C%20Chung%20Chi%20College!5e0!3m2!1sen!2shk!4v1585296745851!5m2!1sen!2shk" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
</div>
<ul style="list-style: none; padding-inline-start: 0;">
  <li>Economic Research Centre<br>
  Hong Kong Institute of Asia-Pacific Studies<br>
  The Chinese University of Hong Kong<br>
  Shatin, New Territories, Hong Kong<br></li>
  <li>Phone: <a href="tel:+85239436762">(852) 3943 6762</a></li>
  <li>Fax: (852) 2603 5215</li>
  <li>Email: <a href="mailto:EconRC@cuhk.edu.hk">EconRC@cuhk.edu.hk</a></li>
</ul>

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
