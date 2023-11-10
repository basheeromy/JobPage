import Layout from "@/components/layout/Layout"
import UpdateProfile from "@/components/user/UpdateProfile";

export default function UpdateProfilePage({ access_token }) {
  return (
    <Layout title='Update User Profile' >
      <UpdateProfile access_token={access_token} />
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
