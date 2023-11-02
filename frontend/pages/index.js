import Layout from "@/components/layout/Layout"
import Home from "@/components/Home"

import axios from 'axios'

export default function Index({data}) {
  return (
    <Layout>
      <Home data={data} />
    </Layout>
  )
}

export async function getServerSideProps({query}) {

  const keyword = query.keyword || ''
  const location = query.location || ''

  const queryStr = `keyword=${keyword}&location=${location}`

  const res = await axios.get(`http://app:8001/api/jobs?${queryStr}`)
  const data = res.data

  return {
    props: {
      data,
    }
  }
}