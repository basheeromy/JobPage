import Layout from "@/components/layout/Layout"
import UploadResume from "@/components/user/UploadResume";

export default function UploadResumePage({ access_token }) {
  return (
    <Layout title='Upload Resume' >
      <UploadResume access_token={access_token} />
    </Layout>
  );
}

export async function getServerSideProps({ req }) {
  const access_token = req.cookies.access;
  return {
    props: {
      access_token,
    },
  };
}