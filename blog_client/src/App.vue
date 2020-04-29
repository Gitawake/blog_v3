<template>
  <div id="app">
    <Row type="flex" justify="center" align="top" class="code-row-bg">
      <Col span="24">
        <template>
          <Menu class="transparent" mode="horizontal" :theme="theme1" active-name="1">
            <MenuItem name="1">
              <Icon type="ios-home"/>
              首页
            </MenuItem>
            <MenuItem name="2">
              <Icon type="md-albums"/>
              分类
            </MenuItem>
            <MenuItem name="3">
              <Icon type="md-pricetags"/>
              标签
            </MenuItem>
            <MenuItem name="4">
              <Icon type="ios-information-circle"/>
              关于
            </MenuItem>
          </Menu>
        </template>
      </Col>
    </Row>
    <Row type="flex" justify="center" align="top" class="code-row-bg">
      <Col span="14" class="row_spacing">
        <Card class="card_padding transparent" :bordered="false">
          <div style="text-align:center">
            <h2><a href="">Vue.js</a></h2>
            <Row type="flex" justify="center" align="top" class="code-row-bg">
              <Col span="3">
                <p>
                  <Icon type="ios-time"/>
                  2020-05-01
                </p>
              </Col>
              <Col span="3">
                <p>
                  <Icon type="md-clipboard"/>
                  2020-05-05
                </p>
              </Col>
              <Col span="2">
                <p>
                  <Icon type="md-albums"/>
                  教程
                </p>
              </Col>
              <Col span="2">
                <p>
                  <Icon type="md-eye"/>
                  18k
                </p>
              </Col>
            </Row>
            <img src="./assets/Desert.jpg" width="100%"/>
            <p>A high quality UI Toolkit based on Vue.jsA high quality UI Toolkit based on Vue.jsA high quality UI
              Toolkit based on Vue.jsA high quality UI Toolkit based on Vue.jsA high quality UI Toolkit based on Vue.jsA
              high quality UI Toolkit based on Vue.jsA high quality UI Toolkit based on Vue.jsA high quality UI Toolkit
              based on Vue.jsA high quality UI Toolkit based on Vue.jsA high quality UI Toolkit based on Vue.jsA high
              quality UI Toolkit based on Vue.jsA high quality UI Toolkit based on Vue.js</p>
            <template>
              <Tag color="default">default</Tag>
              <Tag color="primary">primary</Tag>
              <Tag color="success">success</Tag>
              <Tag color="error">error</Tag>
              <Tag color="warning">warning</Tag>
              <Tag color="magenta">magenta</Tag>
              <Tag color="red">red</Tag>
              <Tag color="volcano">volcano</Tag>
              <Tag color="orange">orange</Tag>
              <Tag color="gold">gold</Tag>
              <Tag color="yellow">yellow</Tag>
              <Tag color="lime">lime</Tag>
              <Tag color="green">green</Tag>
              <Tag color="cyan">cyan</Tag>
              <Tag color="blue">blue</Tag>
              <Tag color="geekblue">geekblue</Tag>
              <Tag color="purple">purple</Tag>
              <Tag color="#FFA2D3">Custom Color</Tag>
            </template>
          </div>
        </Card>
      </Col>
    </Row>
    <template>
      <BackTop></BackTop>
    </template>
    <Row type="flex" justify="center" align="top" class="code-row-bg">
      <Col span="24" class="row_spacing">
        <Footer class="transparent">
          <p>Gardener Blog<br/>
            <small>© 2019 Copyright comes from the gardener's blog.</small>
          </p>
        </Footer>
      </Col>
    </Row>


    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        theme1: 'light'
      }
    }
  }
</script>

<style>
  #app {
    background: url("assets/81035768_p0.png")no-repeat;
    width: 100%;
    height:100%;
    overflow: hidden;
    background-size:cover;
  }

  .row_spacing {
    padding-top: 15px;
  }

  .card_padding {
    margin-bottom: 15px;
  }
  .transparent {
    background: #ffffff7d;
  }

</style>
