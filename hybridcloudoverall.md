# Hybrid Cloud Overall 




### 용어 정리

`일부 자료 출처` [Bespin Global - 새로운 클라우드 시대를 따라잡기 위한 최신 클라우드 용어 정의하기](https://www.bespinglobal.com/cloud-terms-organization/)

1. **Multi Cloud**

   > 같은 종류의 클라우드 서비스를 여러 개의 퍼블릭 클라우드 벤더를 통해 사용하는 것. 비슷한 워크로드[^1]를 여러 벤더에 나눠 사용

   - 배경
     1. [세계 1위 아마존 클라우드 먹통에 국내 유통·게임 올스톱(2018.11.23)]( https://news.joins.com/article/23149450) 
     2. A사 장애 사례 후 복수의 클라우드 서비스를 활용하는 방안 등이 대책으로 거론
     3. 멀티클라우드 환경에선 한 클라우드에서 운영 중단이 발생했을 때 기업을 보호해줄 수 있음
   - 이점
     - 이식성 - 레이턴시 등 이유로 한 호스팅 환경에서 다른 호스팅 환경으로 이동해 고가용성 유지 가능
     - 벤더 독립성 - 각 클라우드 인프라가 가진 특화 기능 사용 가능해짐
     - ..

   ![MC](C:\Users\10151147\Desktop\인턴 교육사항\MC.png)

2. **Hybrid Cloud**

   > Private Cloud, On-Premises와 Public Cloud 서비스를 통합해, 병행하거나, 연동되거나, 상호보완적인 업무를 지원하는 것

   - 배경

     1. 기업들은 자기 부지에 Legacy 설비를 설치하고(Private Cloud, On-Premises) 운영해왔음
     2. 클라우드 비용/운영 효율성을 보고 Public Cloud로 들어옴
        1. 하지만 클라우드 임대료가 직접하는 것보다 비싸다고 느꼈으며
        2. 민감한 기업정보는 Private Cloud, On-Premises에 유지하고 일부 애플리케이션만 Public Cloud에 두고 싶어함
        3. 기존 미션/보안 크리티컬한 업무들은 온프레미스를 벗어나기 어려움 + 정부 규제 산업
     3. 이러한 니즈가 Hybrid Cloud의 형태로 나타남

   - 이점

     - Public Cloud - 급변하는 비즈니스 환경 변황 유연하게 대응, 신속한 자원 도입/확장 가능

     - Private Cloud, On-Premises  - 안정성, 신뢰성, 각종 규제 및 사내 컴플라이언스 이슈 원활한 수용

     - ...

       ​						![HC](C:\Users\10151147\Desktop\인턴 교육사항\HC.png)

   

3. **Hybrid (Multi) Cloud**

   > 여러 개의 Public Cloud를 사용하면서 Private Cloud 인프라를 포함하는 것

   - Hybrid Cloud에서 의미가 확장되어서 Multi Cloud까지 포괄

   

     ![hybrid multi cloud에 대한 이미지 검색결과](https://jelecos.com/wp-content/uploads/2017/03/hybrid-cloud-image-2-1024x665.png)

### Hybrid Cloud 관리 플랫폼 등장

- Gartner 의견[^ 2] 
  - 2022년 까지 80%의 기업들이 Hybrid & Multi Cloud 관리툴을 도입할 예정
  - 기업들은 관리툴 선택에 어려움을 겪고 있으며, 이를 타계하기 위해 자체 솔루션/전문 서비스를 갖춘 3rd Party를 활용 중
  - 많은 장비 벤더사들은 자사의 장비와 관리툴을 통합하여 제공하고 있음
  - 인프라 관리 포함 Orchestrator 서비스를 제공하며 Cloud/Container 워크로드 관리가 목표
- Samsung SDS
  - Global One View : 대시보드, 자원효율화[^3 ], 통합 보안 관제기능, 멀티클라우드+SDS Cloud+Baremetal 자원 현황 확인
- Megazone Cloud
  - Hyper Solutions : 비용 최적화,  보안관제, 최적화 자원 추천  등
- Bespin Global
  - OpsNow : 하이브리드 환경 관리, 모니터링, 자원 현황분석, 비용 최적화, 이벤트 관리 등
- 그외 글로벌 오픈소스 및 솔루션



### 참고 문헌

[Workloads in Cloud Computing]( http://www.somic.org/2010/02/16/workloads-in-cloud-computing/ )

[Bespin Global - 새로운 클라우드 시대를 따라잡기 위한 최신 클라우드 용어 정의하기](https://www.bespinglobal.com/cloud-terms-organization/)

[RedHat - 멀티클라우드란 무엇일까요?]( https://www.redhat.com/ko/topics/cloud-computing/what-is-multicloud )





### 주석

[^1]: Workload is an abstraction of the actual work that your instance or a set of instances are going to perform. Running a web server or a web server farm, or being a Hadoop data node - these are all valid workloads
[^ 2]: 세계적인 IT 시장 분석/컨설팅 업체
[^ 3]: 자원 축소, 스케쥴링, RI, Spot Inst, 예측 기능 등

