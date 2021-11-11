import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Laboratório de Computação de Alto Desempenho</title>
        <link rel="icon" href="logo.png" />
      </Head>
    </div>
  )
}
